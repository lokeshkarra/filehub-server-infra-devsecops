
resource "aws_iam_instance_profile" "ec2_profile" {
  name = "filehub-ec2-profile"
  role = var.iam_role_name
}

resource "aws_instance" "k3s_server" {
  ami                         = "ami-0f58b397bc5c1f2e8"
  instance_type               = "t3.micro"
  subnet_id                   = var.subnet_id
  associate_public_ip_address = true
  key_name                    = var.key_pair_name
  iam_instance_profile        = aws_iam_instance_profile.ec2_profile.name
  vpc_security_group_ids      = [aws_security_group.k3s_sg.id]
  user_data                   = file("${path.module}/user_data/install_k3s.sh")

  tags = {
    Name = "k3s-server"
  }
}

resource "aws_security_group" "k3s_sg" {
  name        = "k3s-sg"
  description = "Allow SSH and K3s traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 6443
    to_port     = 6443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "instance_public_ip" {
  value = aws_instance.k3s_server.public_ip
}
