#!/usr/bin/env python3

"""
Example
 ./LaunchResizeCNExample.py -d kWVD:US-ASHBURN-AD-3 -s ocid1.subnet.oc1.iad.aaaaaaaayavmv5je56izl3zngub7qlsmjashsve5g7ceoanoim76fvvqo5pq -i ocid1.image.oc1..aaaaaaaacx3y4fvrg2m3wibapxu5mgyp64l7nxqo2rhrejprvzfjbhdn747q -c ocid1.compartment.oc1..aaaaaaaabuxnlneozce5wyqugcgextdk24nirx65jr5qm3zjy3ytuxbmgbna
Ref: https://github.com/oracle/oci-python-sdk/blob/master/examples/cluster_networks_example.py
API: https://docs.oracle.com/en-us/iaas/tools/python/2.45.1/api/core/client/oci.core.ComputeManagementClient.html

The code sample does the following:
1. Launches a cluster of size N=1 with shape BM.HPC2.36
2. Resizes it to N=2
3. Terminates the cluster
"""
import time

import oci
import argparse
from oci.core import ComputeManagementClient, ComputeManagementClientCompositeOperations
from oci.core.models import CreateInstanceConfigurationDetails, \
    InstanceConfigurationLaunchInstanceDetails, \
    InstanceConfigurationInstanceSourceViaImageDetails, \
    InstanceConfigurationCreateVnicDetails, \
    ComputeInstanceDetails, \
    InstanceConfigurationBlockVolumeDetails, \
    InstanceConfigurationCreateVolumeDetails, \
    InstanceConfigurationIscsiAttachVolumeDetails, \
    CreateClusterNetworkDetails, \
    ClusterNetworkPlacementConfigurationDetails, \
    CreateClusterNetworkInstancePoolDetails, UpdateClusterNetworkDetails, \
    UpdateClusterNetworkInstancePoolDetails


def _create_block_volume_details(compartment_id, ad):
    """Sets up the model for a simple 50gb BV for use by tests.
    :returns: InstanceConfigurationBlockVolumeDetails
    """
    block_volume_details = InstanceConfigurationBlockVolumeDetails()

    create_volume_details = InstanceConfigurationCreateVolumeDetails()
    create_volume_details.display_name = "blockvol1"
    create_volume_details.compartment_id = compartment_id
    create_volume_details.size_in_gbs = 50
    create_volume_details.availability_domain = ad

    volume_attach_details = InstanceConfigurationIscsiAttachVolumeDetails()

    block_volume_details.create_details = create_volume_details
    block_volume_details.attach_details = volume_attach_details
    return block_volume_details


#  === Main ===

if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--compartment-id',
                        help='Your compartment OCID',
                        required=True
                        )
    parser.add_argument('-d', '--availability-domain',
                        help='the AD where the cluster network will be spun up (cluster network only spans a single AD)',
                        required=True
                        )

    parser.add_argument('-s', '--subnet-id',
                        help='the ',
                        required=True
                        )

    parser.add_argument('-i', '--image-id',
                        help='the image ID to use for instances',
                        required=True
                        )

    args = parser.parse_args()

    # Load the default configuration - use config or Resource Principals
    #config = oci.config.from_file()
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    computeClient = oci.core.ComputeClient(config={}, signer=signer)

    # Step 1 - create the compute management client
    # https://docs.oracle.com/en-us/iaas/tools/python/2.45.1/api/core/client/oci.core.ComputeManagementClient.html
    #compute_management_client = ComputeManagementClient(config)
    compute_management_client = ComputeManagementClient(config={}, signer=signer)
    composite_client = ComputeManagementClientCompositeOperations(compute_management_client)

    # Step 2 - prepare the launch details - Instance Configuration, Instance details
    shape = "BM.HPC2.36"
    launch_details = InstanceConfigurationLaunchInstanceDetails(
        compartment_id=args.compartment_id,
        display_name="example",
        shape=shape,
        source_details=InstanceConfigurationInstanceSourceViaImageDetails(
            image_id=args.image_id
        ),
        create_vnic_details=InstanceConfigurationCreateVnicDetails()
    )

    instance_details = ComputeInstanceDetails(
        launch_details=launch_details,
        block_volumes=[
            _create_block_volume_details(args.compartment_id, args.availability_domain)
        ])

    create_instance_config_details = CreateInstanceConfigurationDetails(
        display_name="sample instance config name",
        compartment_id=args.compartment_id,
        instance_details=instance_details)

    try:

        input("=== Press any key continue to start cluster creation ===")

        # Step 4 - Creates an instance configuration to use with cluster network
        instance_config = compute_management_client.create_instance_configuration(
            create_instance_config_details).data
        # print("Created instanceConfiguration: ", instance_config)
        print("[INFO] Created instanceConfiguration: ", instance_config.id)

        # Step 5 -  Creates a placement configuration for pool
        placement_config = ClusterNetworkPlacementConfigurationDetails()
        placement_config.availability_domain = args.availability_domain
        placement_config.primary_subnet_id = args.subnet_id

        instance_pool_def = CreateClusterNetworkInstancePoolDetails()
        instance_pool_def.instance_configuration_id = instance_config.id
        # Hard code to size 1
        instance_pool_def.size = 1

        create_cluster_network_details = CreateClusterNetworkDetails()
        create_cluster_network_details.compartment_id = args.compartment_id
        create_cluster_network_details.display_name = "sample cluster network"
        create_cluster_network_details.instance_pools = [instance_pool_def]
        create_cluster_network_details.placement_configuration = placement_config

        # Step 6 - Create a cluster network.
        # print("Creating cluster network: ", create_cluster_network_details)
        print("[INFO] Starting to create cluster network..")
        cluster_network = composite_client.create_cluster_network_and_wait_for_state(
            create_cluster_network_details, wait_for_states=["RUNNING"]).data
        # print("Created cluster network: ", cluster_network)
        cluster_id = cluster_network.id
        print("[INFO] Created cluster network: ", cluster_id)

        input(f"=== PAUSE - Check CN {cluster_id} created in console and when ready press any key to continue resize to 2 ===")

        # Step 7 - Update size - Update Instance Pool Details for CN
        cluster_network_response = compute_management_client.get_cluster_network(
            cluster_network_id=cluster_network.id)
        pool_id = cluster_network_response.data.instance_pools[0].id
        current_size_cn = cluster_network_response.data.instance_pools[0].size

        # hardcoded value
        size = 2
        print(f"[INFO] pool_id:{pool_id} current pool_size:{current_size_cn} next_size : {size}")
        instance_pools_details = UpdateClusterNetworkInstancePoolDetails(
            id=pool_id,
            size=size)
        update_cluster_network_details = UpdateClusterNetworkDetails(
            instance_pools=[instance_pools_details],
        )

        print("[INFO] Resizing cluster network...")
        composite_client.update_cluster_network_and_wait_for_state(
            cluster_network_id=cluster_id,
            update_cluster_network_details=update_cluster_network_details,
            wait_for_states=["RUNNING"],
        )
        input("=== Finished resizing... Check console to confirm. Press any key to terminate cluster ===")
    finally:

        # Step 7 - cleaning up created resources
        print("[INFO] Terminating cluster.....")
        compute_management_client.terminate_cluster_network(cluster_network.id)
        print(f"=== Terminated cluster network: {cluster_network}")
