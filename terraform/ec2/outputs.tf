output "k3s_public_ip" {
  value = aws_instance.k3s_server.public_ip
}
output "k3s_instance_id" {
  value = aws_instance.k3s_server.id
}