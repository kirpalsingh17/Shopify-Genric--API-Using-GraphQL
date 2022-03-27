# Shopify Genric API Using GraphQL


<pre>
"query":"query getFileUrl($id: ID!) {
			node(id: $id) {
				... on GenericFile {
							id
							url
							}
					}
			}	
</pre>

<pre>
"variables":{
		"id":"gid://shopify/GenericFile/25822065655964"
		}
</pre>

<pre>
headers = {
  'X-Shopify-Access-Token': 'add you key',
  'Content-Type': 'application/json'
}
</pre>

<pre>
conn.request("POST", "/admin/api/2022-01/graphql.json", payload, headers)
</pre>