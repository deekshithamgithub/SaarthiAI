import 'package:flutter/material.dart';
import '../services/api_service.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String output = "";

  void send() async {
    var res = await ApiService.send("send 2000");
    setState(() {
      output = res;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Saarthi AI")),
      body: Column(
        children: [
          ElevatedButton(onPressed: send, child: Text("Speak")),
          Text(output)
        ],
      ),
    );
  }
}