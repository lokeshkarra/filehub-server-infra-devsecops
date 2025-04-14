

# Eks configuration

module "vpc" {
  source             = "./vpc"
  vpc_name           = "filehub-vpc"
  vpc_cidr           = "10.0.0.0/16"
  availability_zones = ["ap-south-1a", "ap-south-1b"]
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets    = []
}

module "iam" {
  source    = "./iam"
  role_name = "filehub-ec2-admin-role" # changed to reflect EC2 purpose
}


# Remember to uncomment the EKS module when you want to deploy it. I have commented it out to avoid unnecessary costs.

module "eks" {
  source       = "./eks"
  cluster_name = var.cluster_name
  vpc_id       = module.vpc.vpc_id
  subnet_ids   = module.vpc.public_subnets

  

}  

/*
# block if you want to deploy EC2 instances

variable "key_pair_name" {
  description = "EC2 key pair name"
  type        = string
}

module "vpc" {
  source             = "./vpc"
  vpc_name           = "filehub-vpc"
  vpc_cidr           = "10.0.0.0/16"
  availability_zones = ["ap-south-1a", "ap-south-1b"]
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets    = []
}

module "iam" {
  source    = "./iam"
  role_name = "filehub-ec2-admin-role"
}

module "ec2" {
  source            = "./ec2"
  key_pair_name     = var.key_pair_name
  subnet_id         = module.vpc.public_subnets[0]
  vpc_id            = module.vpc.vpc_id
  iam_role_name     = module.iam.ec2_role_name
} */