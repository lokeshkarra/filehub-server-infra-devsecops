module "vpc" {
  source             = "terraform-aws-modules/vpc/aws"
  version            = "4.0.2"

  name               = var.vpc_name
  cidr               = var.vpc_cidr
  azs                = var.availability_zones
  public_subnets     = var.public_subnets
  private_subnets    = var.private_subnets

  enable_nat_gateway = false
  single_nat_gateway = false
  enable_vpn_gateway = false

  create_igw         = true
  map_public_ip_on_launch = true   
  enable_dns_hostnames   = true
  enable_dns_support     = true

  tags = {
    Name = var.vpc_name
  }
}
