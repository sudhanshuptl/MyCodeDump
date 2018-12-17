# What is terraform.?
Terraform is an infrastructure as code software by HashiCorp. It allows users to define a datacenter infrastructure in a high-level configuration language, from which it can create an execution plan to build the infrastructure such as OpenStack[3] or in a service provider such as AWS etc.

# Why ?
* Provide coding workflow to create infrastructure.
* Human readable configuration
* HCl include full json parser for machine generated configuration.

# so the main benefits of Terraform are.
* **Infrastructure as** ```Code : Infrastructure is described using a high-level configuration syntax.```
* **Execution Plans** : ```Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. ```
* **Resource Graph** : 
```Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.```
* **Change Automation** : ```
Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.```
