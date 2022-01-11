#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sys/socket.h"
#include "netinet/in.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "tcp_server");
  
  ros::NodeHandle nh;
  ros::Publisher server_pub = nh.advertise<std_msgs::String>("server", 1000);
  std_msgs::String message;
  std::stringstream ss;
  
  ros::Rate loop_rate(10);
  
  // Socket https://www.linuxhowtos.org/C_C++/socket.htm
  int sockfd, newsockfd, portno, n;
  socklen_t clilen;
  char buffer[256];
  struct sockaddr_in serv_addr, cli_addr;
  
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  if(sockfd < 0){
	  ROS_INFO("Error opening socket");
  }
  
  bzero((char *) &serv_addr, sizeof(serv_addr));
  portno = 5560;
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(portno);
  serv_addr.sin_addr.s_addr = INADDR_ANY;
  if (bind(sockfd,  (struct sockaddr *) &serv_addr, sizeof(serv_addr))<0){
	ROS_INFO("Error on binding");
  }
  listen(sockfd,5);
  clilen = sizeof(cli_addr);
  newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
  if (newsockfd < 0){
	  ROS_INFO("Error on accept");
  }
  
  
  while (ros::ok())
  {
	  bzero(buffer,256);
	  n = read(newsockfd, buffer, 255);
	  if (n < 0){
		  ROS_INFO("Error reading from socket");
	  }
	  ROS_INFO("Here is the message: %s", buffer);
	  n = write(newsockfd,"I got your message", 18);
	  if (n< 0){
		  ROS_INFO("Error writing to socket");
	  } 
	  
	  if(buffer == "KILL"){
	    ROS_INFO("Server kill request");
	  }else{
	    ROS_INFO("Data to publish: %S", buffer);
	    ss << buffer;
	    message.data = ss.str();
	    server_pub.publish(message);
	  }
	  
	  //ros::spinOnce();
	  //loop_rate.sleep();
  }
  return 0;
}
