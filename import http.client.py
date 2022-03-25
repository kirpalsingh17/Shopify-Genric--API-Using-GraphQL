import http.client
import json

conn = http.client.HTTPSConnection("demo-store.myshopify.com")
payload = "{\"query\":\"query getFileUrl($id: ID!) {\\n    node(id: $id) {\\n        ... on GenericFile {\\n            id\\n            url\\n        }\\n    }\\n}\",\"variables\":{\"id\":\"gid://shopify/GenericFile/25822065655964\"}}"
headers = {
  'X-Shopify-Access-Token': 'add you key',
  'Content-Type': 'application/json'
}
conn.request("POST", "/admin/api/2022-01/graphql.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))