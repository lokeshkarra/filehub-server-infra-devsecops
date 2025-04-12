# output "node_role_arn" {
#   value = aws_iam_role.eks_node_role.arn
# }


output "ec2_role_name" {
  value = aws_iam_role.ec2_role.name
}
