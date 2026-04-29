import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<String> send(String text) async {
    var res = await http.post(
      Uri.parse("http://127.0.0.1:8000/process"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"text": text, "user_id": "user123"}),
    );

    return res.body;
  }
}
