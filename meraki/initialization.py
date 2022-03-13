import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY ='8edf90ea5b8cb679d072148fcfffb3457e624fdb'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)
org = dashboard.organizations.getOrganizations()
org_id=org[0]['id']
print(org_id)
