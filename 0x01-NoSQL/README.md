# 0x01. NoSQL
## Resources
### Read or watch:
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)

### What is NoSQL?
NoSQL is an approach to databases that represents a shift away from traditional relational database management systems (RDBMS). To define NoSQL, it is helpful to start by describing SQL, which is a query language used by RDBMS. Relational databases rely on tables, columns, rows, or schemas to organize and retrieve data. In contrast, NoSQL databases do not rely on these structures and use more flexible data models. NoSQL can mean “not SQL” or “not only SQL.” As RDBMS have increasingly failed to meet the performance, scalability, and flexibility needs that next-generation, data-intensive applications require, NoSQL databases have been adopted by mainstream enterprises. NoSQL is particularly useful for storing unstructured data, which is growing far more rapidly than structured data and does not fit the relational schemas of RDBMS. Common types of unstructured data include: user and session data; chat, messaging, and log data; time series data such as IoT and device data; and large objects such as video and images.
### Types of NoSQL Databases
1. **Key-value data stores:**
Key-value NoSQL databases emphasize simplicity and are very useful in accelerating an application to support high-speed read and write processing of non-transactional data. Stored values can be any type of binary object (text, video, JSON document, etc.) and are accessed via a key. The application has complete control over what is stored in the value, making this the most flexible NoSQL model. Data is partitioned and replicated across a cluster to get scalability and availability. For this reason, key value stores often do not support transactions. However, they are highly effective at scaling applications that deal with high-velocity, non-transactional data.
2. **Document stores:**
Document databases typically store self-describing JSON, XML, and BSON documents. They are similar to key-value stores, but in this case, a value is a single document that stores all data related to a specific key. Popular fields in the document can be indexed to provide fast retrieval without knowing the key. Each document can have the same or a different structure.
3. **Wide-column stores:**
Wide-column NoSQL databases store data in tables with rows and columns similar to RDBMS, but names and formats of columns can vary from row to row across the table. Wide-column databases group columns of related data together. A query can retrieve related data in a single operation because only the columns associated with the query are retrieved. In an RDBMS, the data would be in different rows stored in different places on disk, requiring multiple disk operations for retrieval.
4. **Graph stores:**
A graph database uses graph structures to store, map, and query relationships. They provide index-free adjacency, so that adjacent elements are linked together without using an index.
### Benefits of NoSQL
**NoSQL databases offer enterprises important advantages over traditional RDBMS, including:**

- **Scalability:**
NoSQL databases use a horizontal scale-out methodology that makes it easy to add or reduce capacity quickly and non-disruptively with commodity hardware. This eliminates the tremendous cost and complexity of manual sharding that is necessary when attempting to scale RDBMS.
- **Performance:**
By simply adding commodity resources, enterprises can increase performance with NoSQL databases. This enables organizations to continue to deliver reliably fast user experiences with a predictable return on investment for adding resources—again, without the overhead associated with manual sharding.
- **High Availability:**
NoSQL databases are generally designed to ensure high availability and avoid the complexity that comes with a typical RDBMS architecture that relies on primary and secondary nodes. Some “distributed” NoSQL databases use a masterless architecture that automatically distributes data equally among multiple resources so that the application remains available for both read and write operations even when one node fails.
- **Global Availability:**
 By automatically replicating data across multiple servers, data centers, or cloud resources, distributed NoSQL databases can minimize latency and ensure a consistent application experience wherever users are located. An added benefit is a significantly reduced database management burden from manual RDBMS configuration, freeing operations teams to focus on other business priorities.
- **Flexible Data Modeling:**
NoSQL offers the ability to implement flexible and fluid data models. Application developers can leverage the data types and query options that are the most natural fit to the specific application use case rather than those that fit the database schema. The result is a simpler interaction between the application and the database and faster, more agile development.

### Aggregation Operations
**Aggregation operations process multiple documents and return computed results. You can use aggregation operations to:**

- Group values from multiple documents together.
- Perform operations on the grouped data to return a single result.
- Analyze data changes over time.

**To perform aggregation operations, you can use:**

- [Aggregation pipelines](https://www.mongodb.com/docs/manual/aggregation/#std-label-aggregation-pipeline-intro), which are the preferred method for performing aggregations.
- [Single purpose aggregation methods](https://www.mongodb.com/docs/manual/aggregation/#std-label-single-purpose-agg-methods), which are simple but lack the capabilities of an aggregation pipeline.
### Aggregation Pipelines
**An aggregation pipeline consists of one or more [stages](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/#std-label-aggregation-pipeline-operator-reference) that process documents:**

- Each stage performs an operation on the input documents. For example, a stage can filter documents, group documents, and calculate values.
- The documents that are output from a stage are passed to the next stage.
- An aggregation pipeline can return results for groups of documents. For example, return the total, average, maximum, and minimum values.

You can update documents with an aggregation pipeline if you use the stages shown in Updates with Aggregation Pipeline.

### Aggregation Pipeline Example

The following aggregation pipeline example contains two stages and returns the total order quantity of medium size pizzas grouped by pizza name:

```JavaScript
db.orders.aggregate( [
   // Stage 1: Filter pizza order documents by pizza size
   {
      $match: { size: "medium" }
   },
   // Stage 2: Group remaining documents by pizza name and calculate total quantity
   {
      $group: { _id: "$name", totalQuantity: { $sum: "$quantity" } }
   }
] )
```
The [$match](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match)stage:

- Filters the pizza order documents to pizzas with a size of medium.
- Passes the remaining documents to the $group stage.

The [$group](https://www.mongodb.com/docs/manual/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage:

- Groups the remaining documents by pizza name.
- Uses $sum to calculate the total order quantity for each pizza name. The total is stored in the totalQuantity field returned by the aggregation pipeline.

### Aggregation Stages
- In the db.collection.aggregate() method and db.aggregate() method, pipeline stages appear in an array. In the Atlas UI, you can arrange pipeline stages using the aggregation pipeline builder. Documents pass through the stages in sequence.

### MongoDB Shell
The MongoDB Shell, mongosh, is a JavaScript and Node.js REPL environment for interacting with MongoDB deployments in Atlas  , locally, or on another remote host. Use the MongoDB Shell to test queries and interact with the data in your MongoDB database.

### Access MongoDB From Your Shell
#### Connect to MongoDB
Connect to a MongoDB deployment using the connection string.

The following connection string connects to an Atlas deployment:
```shell
mongosh "mongodb+srv://mycluster.abcd1.mongodb.net/myFirstDatabase" --apiVersion 1 --username <username>
```

mongosh supports common insert opererations, including:
- db.collection.insertOne()
- db.collection.insertMany()

Use the db.collection.find() method to query documents in a collection.

mongosh supports common update operations, including:
- db.collection.updateOne()
- db.collection.updateMany()
- db.collection.replaceOne()

#### Delete Documents
mongosh supports common delete operations, including:
- db.collection.deleteMany()
- db.collection.deleteOne()

You can run aggregation pipelines in mongosh using the db.collection.aggregate() method. Aggregation pipelines transform your documents into aggregated results based on the stages you specify.