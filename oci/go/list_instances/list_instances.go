package main

import (
	"context"
	"fmt"
	"github.com/oracle/oci-go-sdk/v51/common"
	"github.com/oracle/oci-go-sdk/v51/core"
	_ "github.com/oracle/oci-go-sdk/v51/core"
)

func main() {
	client, _ := core.NewComputeClientWithConfigurationProvider(common.DefaultConfigProvider())
	req := core.ListInstancesRequest{
		CompartmentId: common.String("ocid1.compartment.oc1..aaaaaaaa2bv45q4vcdc6e4otblyllu4itrsblspvicblqanhwn6q2fhefibq"),
	}
	resp, _ := client.ListInstances(context.Background(), req)

	fmt.Println(resp)
	return
}