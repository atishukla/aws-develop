## Playing with dynamo db

- To find all the projects that Atishay is part of
We have to use **inverted Index** from indexes tab in dynamo db

### GSI Overloading
- One table can have same attribute saving different kind of data
- It can store name, salary and date
- We will set up the unique prefix for data and then use it to query
- It saves cost

### use case for GSI
- In our example instead of using id or organisation and employee we should be able to list with names
- This should be possible with GSI

### How to
- Create a common attribute **Data**
- We prefix data with some part like ORG# for organisation, PRO# with project name, and EMP# with employee
- For GSI we will keep the **same partition key PK** for the table for new **data** attribute as the sort key