# Configs can be set in Configuration class directly or using helper utility
from kubernetes import client, config


config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing Pods:")
print("____________________________")
ret = v1.list_namespaced_pod('default', watch=False)
for i in ret.items:
 
   print("\nPod name: "+ i.metadata.name + "\nPod ID: " + i.metadata.uid)

     
v1.delete_namespaced_pod(name="jj4", namespace="default", body=client.V1DeleteOptions())

print("---------------------")   
print("\nPod jj4 is deleted...\n")
print("---------------------")   


print("\nRemaining Pods: ")
print("____________________________")
for i in ret.items:
	print( i.metadata.name)


