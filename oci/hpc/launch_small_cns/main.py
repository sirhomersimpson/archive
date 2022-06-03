import oci
import time
from datetime import datetime
from oci.config import validate_config

from oci.core import ComputeManagementClient, ComputeManagementClientCompositeOperations, ComputeClient
from oci.core.models import CreateClusterNetworkDetails, \
    ClusterNetworkPlacementConfigurationDetails, \
    CreateClusterNetworkInstancePoolDetails

OCI_CONFIG_FILE = "~/.oci/config"
#OCI_PROFILE = "HPC_RIK_DEFAULT"
OCI_PROFILE = "HPC_RKISNAH_R1"


# Number of CNs
NUM_CNS = 8
# Size of cluster
CLUSTER_SIZE = 1
# Time to sleep between
SLEEPY = 0
# Configurations / Set up
config = oci.config.from_file(OCI_CONFIG_FILE, OCI_PROFILE)
compartment_id = config["compartment"]
availability_domain = config["ad"]
instance_config_id = config["ic"]
subnet_id = config["subnet_id"]

compute_management_client = ComputeManagementClient(config)
composite_client = ComputeManagementClientCompositeOperations(compute_management_client)
compute_client = ComputeClient(config)
work_requests_client = oci.work_requests.WorkRequestClient(config)


validate_config(config)


def launch_cluster(num_of_cns):
    placement_configuration_details = ClusterNetworkPlacementConfigurationDetails(
        availability_domain=availability_domain,
        primary_subnet_id=subnet_id,
    )
    instance_pool_details = CreateClusterNetworkInstancePoolDetails(
        instance_configuration_id=instance_config_id,
        size=CLUSTER_SIZE,
    )
    for count in range(num_of_cns):
        create_cluster_network_details = CreateClusterNetworkDetails(
            compartment_id=compartment_id,
            instance_pools=[instance_pool_details],
            placement_configuration=placement_configuration_details,
            display_name="0sleep1rik-cluster-" + str(count) + "-hpc",
        )
        response = compute_management_client.create_cluster_network(create_cluster_network_details)
        print(f"{response.data.id}")
        #print(f"Let me sleep now for {SLEEPY} before I go and create another CN")
        time.sleep(SLEEPY)


def find_creation_time_of_cn(list_cn_ocid):
    """
    It gets time to create CN + time to when last BM is created
    """
    list_times = []
    for cn_ocid in list_cn_ocid:
        response_get_cn = compute_management_client.get_cluster_network(cn_ocid)
        cn_time_created = response_get_cn.data.time_created
        cn_size = response_get_cn.data.instance_pools[0].size
        response_get_cn_instances = compute_management_client.list_cluster_network_instances(compartment_id, cn_ocid)
        instance_id = response_get_cn_instances.data[cn_size - 1].id
        time_last_bm_created = find_time_when_bm_is_complete(instance_id)

        # Add all cn_created and bm_create times in a list
        list_times.append(cn_time_created)
        list_times.append(time_last_bm_created)

        diff = time_last_bm_created - cn_time_created
        #print(f'{cn_time_created} {time_last_bm_created}')
        print(f'{cn_ocid} {diff.seconds}')
    list_times.sort()
    diff_all_cns_creation_time = list_times[len(list_times)-1] - list_times[0]
    print(f'Total batch CNs Creation time: {diff_all_cns_creation_time.seconds}')


def find_time_when_bm_is_complete(instance_ocid):
    list_wr_response = work_requests_client.list_work_requests(
        compartment_id=compartment_id,
        resource_id=instance_ocid
    )
    t = list_wr_response.data[2].time_finished
    return t


def terminate_cn(list_cn_ocid):
    for cn_ocid in list_cn_ocid:
        print(cn_ocid)
        compute_management_client.terminate_cluster_network(cn_ocid)


if __name__ == '__main__':
    """
    To get this list via bash 
    for c in ${cns[@]}; do echo \'$c\',; done
    """
    list_cn_ocids = [
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6ya5e7g5xxjx6dw3xmchpcq3qtqqohdm5erc6qzqvvmrfcq",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6yaklxfn32wevitj77hiuidbxwngygx4yeumsq2mopa6fla",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6yarajdod53c5gnalnbtn27rrslxbhfyxj4majq6hclnsha",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6yatws3ufalqk5bkyryf35sipaxy6wag64tcwg2hysvewbq",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6ya5dh2obzcg263g6mwzu4kenwugdkipw3ga4heaouywb6a",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6ya4mlqefbc6u7urzqr2u56vnhvliy46jva2indoysqbuhq",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6ya6mhinuj6k7cmmlsktzkitxvwef733okz23fpjhia6g5a",
        "ocid1.clusternetwork.region1.sea.amaaaaaanjq7b6yaf3ihxhy5e3uzx4whieu7hxqia5yeffofou7d7uzj2kwq",
    ]

    # Step 1 - Launch the CNs
    #launch_cluster(NUM_CNS)
    # Step 2 - List the CNs
    #print(len(list_cn_ocids))
    #find_creation_time_of_cn(list_cn_ocids)
    #Step 3 - Destroy the CNs
    #terminate_cn(list_cn_ocids)
