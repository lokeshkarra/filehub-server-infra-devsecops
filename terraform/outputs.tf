# output "cluster_endpoint" {
#   value = module.eks.cluster_endpoint
# }

# output "cluster_id" {
#   value = module.eks.cluster_id
# }

# output "cluster_name" {
#   value = module.eks.cluster_name
# }

output "k3s_server_public_ip" {
  description = "Public IP of the K3s EC2 instance"
  value       = module.ec2.k3s_public_ip
}

output "k3s_server_id" {
  description = "EC2 instance ID for the K3s server"
  value       = module.ec2.k3s_instance_id
}

output "k3s_server_ssh" {
  description = "SSH command to access the K3s server"
  value       = "ssh -i ~/.ssh/${var.key_pair_name}.pem ubuntu@${module.ec2.k3s_public_ip}"
}

