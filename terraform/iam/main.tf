
 # This Terraform configuration creates an IAM role for EKS worker nodes with the necessary policies attached.
  # It uses the AWS provider to manage IAM resources.


resource "aws_iam_role" "eks_node_role" {
  name = var.role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "eks_worker_node_policy" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_iam_role_policy_attachment" "eks_cni_policy" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
}

resource "aws_iam_role_policy_attachment" "ec2_container_registry_read_only" {
  role       = aws_iam_role.eks_node_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}


# for ec2 instance configuration
# resource "aws_iam_role" "ec2_role" {
#   name               = var.role_name
#   assume_role_policy = data.aws_iam_policy_document.ec2_assume_role_policy.json
# }

# data "aws_iam_policy_document" "ec2_assume_role_policy" {
#   statement {
#     actions = ["sts:AssumeRole"]

#     principals {
#       type        = "Service"
#       identifiers = ["ec2.amazonaws.com"]
#     }
#   }
# }

# resource "aws_iam_role_policy_attachment" "ec2_admin_attach" {
#   role       = aws_iam_role.ec2_role.name
#   policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
# }
