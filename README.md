# P2P FILE TRANSFER

### Purpose & General Info
This is a networking project for me to learn how peer-to-peer network works.<br>
It allows sharing files among peers.<br>
This application is written in python 3.<br>

### What I Learned
1. Difference between client-server network and peer-to-peer network
	Client-server network has dedicated servers that listen to requests from clients. The server does processing of request, logic, assembling and returning data. In a 3-tier system, there is a layer between the client and the server called application server (e.g. the google search engine, which takes a request from the client, index it, then sends the request to other servers).</br>
	P2p is a decentralized model where each node acts as a peer. Unlike the client-server network, there is no dedicated server: Each node can act as both a server and a client. Bandwidth can be shared between peers and the performace improves as more peers join the network. There are more categorization that goes on in the p2p network:<br>
		Centralized vs. Decentralized (Scalable vs. High fault-tolerance)<br>
		Under the decentralized p2p model, there is topology and structure:<br>
			Topology: Structured vs. Unstructured (Low cost vs. Low search time)<br>
			Structure: Flat vs Hierarchical<br>

2. Pros and Cons of p2p network<br>
	Pros:<br>
		- Low cost: There is no need to maintain a powerful server.<br>
		- Fault-tolerant: In a client-server network, if the server fails then the network is down. P2p everyone shares equal rights and priviledges: If one peer fails another peer can be used as a server.<br>
	Cons:<br>
		- Security threats: Distribution of virus, port issues and content pirating<br>
		- Lack of backup: Since there is no centralized location that has all the resources, backups cannot be created and files cannot be indexed. This is why p2p network is not the industry standards for companies.

### How To Run
cd into directory and type
```
python3 p2p.py
```
If you don't have pydub, install it through pip
```
pip3 install pydub
```
