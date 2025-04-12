/*

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "19.21.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.28"

  subnet_ids = var.subnet_ids
  vpc_id     = var.vpc_id

  aws_auth_users = [
    {
      userarn  = "arn:aws:iam::543137179138:user/loki"
      username = "loki"
      groups   = ["system:masters"]
    }
  ]

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.medium"]   # ✅ x86_64 instance
      desired_size   = 1
      max_size       = 1
      min_size       = 1
      capacity_type  = "SPOT"
      ami_type       = "AL2_x86_64"   # ✅ Compatible AMI
    }
  }
  cluster_endpoint_public_access  = true


  tags = {
    Environment = "dev"
  }
}
*/