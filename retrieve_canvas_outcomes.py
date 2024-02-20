import requests
import json

# Canvas GraphQL endpoint - You need to verify the correct endpoint for GraphQL queries in your Canvas instance
GRAPHQL_ENDPOINT = 'https://fhict.instructure.com/api/graphql'

# Your Canvas API access token
ACCESS_TOKEN = '2464~g8F3nAdsjTRY8DSrYNioRVCWapMqMgWbdSc7UwQEQYTQqGm9jOumGvRtnAf8kqcE'

# GraphQL query
query = """
query SearchGroupOutcomesQuery($id: ID!, $outcomesCursor: String, $outcomesContextId: ID!, $outcomesContextType: String!, $searchQuery: String, $targetGroupId: ID) {
  group: legacyNode(type: LearningOutcomeGroup, _id: $id) {
    ... on LearningOutcomeGroup {
      _id
      description
      title
      outcomesCount(searchQuery: $searchQuery)
      notImportedOutcomesCount(targetGroupId: $targetGroupId)
      outcomes(searchQuery: $searchQuery, first: 1000, after: $outcomesCursor) {
        pageInfo {
          hasNextPage
          endCursor
          __typename
        }
        edges {
          canUnlink
          _id
          node {
            ... on LearningOutcome {
              _id
              description
              title
              displayName
              calculationMethod
              calculationInt
              masteryPoints
              ratings {
                description
                points
                __typename
              }
              canEdit
              canArchive(contextId: $outcomesContextId, contextType: $outcomesContextType)
              contextType
              contextId
              friendlyDescription(contextId: $outcomesContextId, contextType: $outcomesContextType) {
                _id
                description
                __typename
              }
              __typename
            }
            __typename
          }
          group {
            _id
            title
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

"""

# Variables for your query (replace with actual values as needed)
variables = {
  "id": "57713",
  "outcomeIsImported": False,
  "outcomesContextType": "Course",
  "outcomesContextId": "13756"
}

# Headers including the authorization token
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Make the POST request to the GraphQL endpoint
response = requests.post(GRAPHQL_ENDPOINT, headers=headers, json={'query': query, 'variables': variables})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()["data"]["group"]["outcomes"]["edges"]
    for kpi in data:
        with open(f"./trainingData/kpis/{kpi['node']['title']}.json", mode="w+") as file:
            file.write(json.dumps(kpi))

    print(json.dumps(response.json(), indent=2))
else:
    print(f"Query failed to run by returning code of {response.status_code}. {response.text}")

    # Print the JSON response
            # with open("CanvasOutcomeData.json", "w") as file:
            #     file.write(json.dumps(data))