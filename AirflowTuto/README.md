# Airflow Tuto

This a simple tuto about airflow from what I learned

## What is DAG?

The **dags** folder refers to the directory where you define and store your Directed Acyclic Graphs (DAGs).

A DAG in Airflow represents a workflow, and it's a Python script that defines the tasks and their execution order. The dags folder is monitored by Airflow, and any DAG files placed in this folder are automatically detected and displayed in the Airflow UI.

By default, the dags folder is located in the AIRFLOW_HOME directory, but you can customize its location in the Airflow configuration file (airflow.cfg) using the `dags_folder` setting.

Inside the `my_dag.py`, you define your DAGs, tasks, and their dependencies.

## What's a Workflow?

A workflow refers to a series of tasks or processes that are organized to achieve a specific outcome. In the context of software, especially in platforms like Apache Airflow, a workflow represents a defined sequence of automated tasks that run in a specified order.

Workflows typically involve:

* **Tasks**: Individual steps or processes that need to be executed (e.g., running scripts, extracting data, sending emails).
* **Dependencies**: The relationships between tasks, defining which tasks need to complete before others can start.
* **Triggers**: Conditions or events that initiate the workflow (e.g., a specific time, external events, or the completion of another task).

## Examples of Workflows:

* **Data Processing Pipeline**: A workflow that collects raw data, processes it, stores it in a database, and generates a report. *(I should work on a project with this)*
* **CI/CD Pipeline**: A workflow that automates software testing, building, and deployment when changes are pushed to a code repository.

## DAG in Airflow

![DAG in Airflow](pics/dag_in_airflow.png)

In Airflow, a DAG is a workflow that organizes and manages a set of tasks and their dependencies. The DAG defines the sequence in which tasks are executed. It's composed of:

* **Nodes**: In Airflow, each node in the graph represents a task (an individual unit of work like running a Python function, a Bash script, or querying a database).
* **Edges**: The edges represent the dependencies between the tasks, indicating the order in which they should run. For example, Task B can only run after Task A is completed.

## How DAGs Work in Airflow:

* **Tasks as Nodes**: Each node in a DAG represents a task. These tasks can be anything that needs to be done, such as processing data, sending an email, or running a machine learning model.

* **Dependencies as Edges**: The edges between the tasks define their dependencies. If Task B depends on Task A, there will be a directed edge from A to B, meaning A must run and finish before B can start.

* **Acyclic Nature**: Since DAGs are acyclic, once Task A has been executed, it will not loop back to run again within the same workflow execution. This ensures that the workflow has a clear beginning and end, and that there are no infinite loops.

    > Task 1: Extract Data --> Task 2: Transform Data --> Task 3: Load Data

Note that there are four task states:

* **Success**: When a task completes successfully, the downstream tasks are executed.
* **Failed**: When a task fails, no further downstream tasks are executed unless retries are defined.
* **Skipped**: If a task’s dependencies aren’t met (e.g., upstream task fails), it can be marked as “skipped.”
* **Upstream Failed**: If an upstream task fails, downstream tasks that depend on it won’t be executed.

## Why Use DAGs in Airflow?

* **Dependency Management**: DAGs clearly define which tasks must run before or after others.
* **Scheduling**: Airflow’s DAGs can be scheduled to run at specific intervals (e.g., daily, hourly).
* **Error Handling**: DAGs allow you to retry failed tasks or stop the entire workflow if a task fails.
* **Parallelism**: Tasks that don't have dependencies on each other can run in parallel, which speeds up the workflow execution.

## What is an Operator?

In Airflow, an operator is a fundamental building block that defines a single task in a Directed Acyclic Graph (DAG). Operators are abstractions for tasks, representing units of work in your workflow. Each operator performs a specific function or action, such as executing a Python function, running a bash command, or transferring data between systems.

## Types of Operators:

1. **Action Operators**: Perform specific actions.
   - **PythonOperator**: Executes a Python function.
   - **BashOperator**: Runs a bash command.
   - **EmailOperator**: Sends an email.
   - **HttpSensor**: Waits for an HTTP response.

2. **Transfer Operators**: Move data between different systems.
   - **S3ToGCSOperator**: Transfers data from AWS S3 to Google Cloud Storage.
   - **MySqlToHiveOperator**: Transfers data from MySQL to Hive.

3. **Sensors**: Special operators that wait for certain conditions to be met before proceeding, like waiting for a file to appear or a certain time.
   - **FileSensor**: Waits for a file to be present.
   - **TimeSensor**: Waits for a specific amount of time.

4. **TaskFlow Operators**: Used in Airflow's TaskFlow API for handling tasks in a functional style.
   - **@task decorator**: Allows defining tasks as Python functions decorated with `@task`.
