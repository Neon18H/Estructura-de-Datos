import 'package:flutter/material.dart';

class Tallas extends StatelessWidget {
  const Tallas ({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
  padding: const EdgeInsets.all(70),
  child: Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
      Container(
        decoration: BoxDecoration(
          border: Border.all(color: Colors.black,
          width: 1,
          ),
          borderRadius:
          BorderRadius.circular(10.0), 
        ),

        child: Column(
          children: [
            Text('10'),
          ],
        ),
      ),
      Container(
        decoration: BoxDecoration(
          border: Border.all(color: Colors.black,
          width: 1,
          ),
          borderRadius: 
          BorderRadius.circular(10.0),
        ),
        child: Column(
          children: [
            Text('10.5'),
          ],
        ),
      ),
      Container(
        width: 50,
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black,
            width: 1,
          ),
          borderRadius: 
          BorderRadius.circular(20.0),
        ),
        child: Column(
          children: [
            Text('11'),
          ],
        ),
      ),
      Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black,
            width: 1,    
          ),
          borderRadius: 
          BorderRadius.circular(20.0),
        ),
        child: Column(
          children: [
            Text('11.5'),
          ],
        ),
      ),
      Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black,
            width: 1,
          ),
          borderRadius:
          BorderRadius.circular(20.0), 
        ),
        child: Column(
          children: [
            Text('12'),
          ],
        ),
      ),
    ],
  ),
);

      
    
  }
}
