// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class CelularrecomendadoStruct extends BaseStruct {
  CelularrecomendadoStruct({
    List<String>? nome,
    List<String>? preco,
    List<String>? imagem,
    List<String>? motivo,
  })  : _nome = nome,
        _preco = preco,
        _imagem = imagem,
        _motivo = motivo;

  // "nome" field.
  List<String>? _nome;
  List<String> get nome => _nome ?? const [];
  set nome(List<String>? val) => _nome = val;

  void updateNome(Function(List<String>) updateFn) {
    updateFn(_nome ??= []);
  }

  bool hasNome() => _nome != null;

  // "preco" field.
  List<String>? _preco;
  List<String> get preco => _preco ?? const [];
  set preco(List<String>? val) => _preco = val;

  void updatePreco(Function(List<String>) updateFn) {
    updateFn(_preco ??= []);
  }

  bool hasPreco() => _preco != null;

  // "imagem" field.
  List<String>? _imagem;
  List<String> get imagem => _imagem ?? const [];
  set imagem(List<String>? val) => _imagem = val;

  void updateImagem(Function(List<String>) updateFn) {
    updateFn(_imagem ??= []);
  }

  bool hasImagem() => _imagem != null;

  // "motivo" field.
  List<String>? _motivo;
  List<String> get motivo => _motivo ?? const [];
  set motivo(List<String>? val) => _motivo = val;

  void updateMotivo(Function(List<String>) updateFn) {
    updateFn(_motivo ??= []);
  }

  bool hasMotivo() => _motivo != null;

  static CelularrecomendadoStruct fromMap(Map<String, dynamic> data) =>
      CelularrecomendadoStruct(
        nome: getDataList(data['nome']),
        preco: getDataList(data['preco']),
        imagem: getDataList(data['imagem']),
        motivo: getDataList(data['motivo']),
      );

  static CelularrecomendadoStruct? maybeFromMap(dynamic data) => data is Map
      ? CelularrecomendadoStruct.fromMap(data.cast<String, dynamic>())
      : null;

  Map<String, dynamic> toMap() => {
        'nome': _nome,
        'preco': _preco,
        'imagem': _imagem,
        'motivo': _motivo,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => toMap();
  static CelularrecomendadoStruct fromSerializableMap(
          Map<String, dynamic> data) =>
      fromMap(data);

  @override
  String toString() => 'CelularrecomendadoStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    const listEquality = ListEquality();
    return other is CelularrecomendadoStruct &&
        listEquality.equals(nome, other.nome) &&
        listEquality.equals(preco, other.preco) &&
        listEquality.equals(imagem, other.imagem) &&
        listEquality.equals(motivo, other.motivo);
  }

  @override
  int get hashCode => const ListEquality().hash([nome, preco, imagem, motivo]);
}

CelularrecomendadoStruct createCelularrecomendadoStruct() =>
    CelularrecomendadoStruct();
