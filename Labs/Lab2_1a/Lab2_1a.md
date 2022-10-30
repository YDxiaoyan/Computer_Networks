In this assignment, you will develop a simple Web server in Python that is capable of processing only one request. 
Specifically, your Web server will 
(i) create a connection socket when contacted by a client (browser); 
(ii) receive the HTTP request from this connection; 
(iii) parse the request to determine the specific file being requested;
(iv) get the requested file from the server’s file system; 
(v) create an HTTP response message consisting of the requested file preceded by header lines; and
(vi) send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message.!
