provider "aws" {
  region = "us-east-1"
}

locals {
  main_s3_bucket = "terraform-backend-bucket-936301010316"
}

terraform {
  backend "s3" {
    bucket         = "terraform-backend-bucket-936301010316"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-table"
  }
}

module "webserver_cluster" {
  source                 = "./modules/servies/webserver-cluster"
  cluster_name           = "webserver-cluster"
  db_remote_state_bucket = local.main_s3_bucket
  db_remote_state_key    = "stage/data-stores/mysql/terraform.tfstate"
  instance_type          = "t2.micro"
  min_size               = 1
  max_size               = 2

}

resource "aws_security_group_rule" "allow_testing_inbound" {
  type              = "ingress"
  security_group_id = module.webserver_cluster.alb_security_group_id

  from_port   = 12345
  to_port     = 12345
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}
