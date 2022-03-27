# Shopify Genric API Using GraphQL

<h2>GraphQL Query</h2>
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

<h2>GraphQL Query Variable</h2>
<pre>
"variables":{
		"id":"gid://shopify/GenericFile/25822065655964"
		}
</pre>


<h2>Header request for Shopify Access token</h2>
<pre>
headers = {
  'X-Shopify-Access-Token': 'add you key',
  'Content-Type': 'application/json'
}
</pre>

<h2>GraphQL POST request</h2>
<pre>
conn.request("POST", "/admin/api/2022-01/graphql.json", payload, headers)
</pre>