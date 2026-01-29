import 'package:flutter/material.dart';
import '/backend/schema/structs/index.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'flutter_flow/flutter_flow_util.dart';
import 'dart:convert';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {}

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  String _objetivoglobal = '';
  String get objetivoglobal => _objetivoglobal;
  set objetivoglobal(String value) {
    _objetivoglobal = value;
  }

  List<dynamic> _listaResultados = [];
  List<dynamic> get listaResultados => _listaResultados;
  set listaResultados(List<dynamic> value) {
    _listaResultados = value;
  }

  void addToListaResultados(dynamic value) {
    listaResultados.add(value);
  }

  void removeFromListaResultados(dynamic value) {
    listaResultados.remove(value);
  }

  void removeAtIndexFromListaResultados(int index) {
    listaResultados.removeAt(index);
  }

  void updateListaResultadosAtIndex(
    int index,
    dynamic Function(dynamic) updateFn,
  ) {
    listaResultados[index] = updateFn(_listaResultados[index]);
  }

  void insertAtIndexInListaResultados(int index, dynamic value) {
    listaResultados.insert(index, value);
  }
}
