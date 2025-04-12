
variable "key_pair_name" {
  description = "EC2 key pair name"
  type        = string
  default     = "k8onec2" # <-- Your key pair name
}


variable "subnet_id" {
  description = "Subnet ID to launch the EC2 instance in"
  type        = string
}



variable "vpc_id" {
  description = "VPC ID where the EC2 instance will be launched"
  type        = string
  
}

variable "iam_role_name" {
  description = "IAM role name for the EC2 instance"
  type        = string
  
}