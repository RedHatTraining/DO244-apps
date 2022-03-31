== Ping v1

HTTP -> endpoint-func (python) -> [event] -> Broker -> event-consumer (python)

* endpoint-func: `kn func create -l python -t http endpoint-func`
* event-consumer: `kn func create -l python -t cloudevents event-consumer`

0) Create OCP project
1) Create broker (resources/broker.yaml)  
`oc apply -f resources/broker.yaml`
2) Get Broker URL  
`oc get broker`
3) Update `endpoint-func/func.yaml` with the broker URL (as env)
```
...
buildEnvs: []
envs:
  - name: BROKER_URL
    value: http://...svc.cluster.local/ping-v1/ping-broker
annotations: {}
...
```
4) Deploy `event-consumer`  
`kn func deploy`
5) Create a Trigger (resources/trigger.yaml)  
`oc apply -f resources/trigger.yaml`
6) Deploy `endpoint-func`  
`kn func deploy`




----

(venv) [psolarvi@psolarvi endpoint-func]$ kn func delete

🕐 Removing Knative Service 'ping-v1' and all dependent resources

Error: error deleting resources:
 pipelineruns.tekton.dev is forbidden: User "developer" cannot deletecollection resource "pipelineruns" in API group "tekton.dev" at the cluster scope
 pipelines.tekton.dev is forbidden: User "developer" cannot deletecollection resource "pipelines" in API group "tekton.dev" at the cluster scope
