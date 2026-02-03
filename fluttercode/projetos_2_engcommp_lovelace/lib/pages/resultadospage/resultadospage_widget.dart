import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'resultadospage_model.dart';
export 'resultadospage_model.dart';

class ResultadospageWidget extends StatefulWidget {
  const ResultadospageWidget({super.key});

  static String routeName = 'resultadospage';
  static String routePath = '/resultadospage';

  @override
  State<ResultadospageWidget> createState() => _ResultadospageWidgetState();
}

class _ResultadospageWidgetState extends State<ResultadospageWidget> {
  late ResultadospageModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => ResultadospageModel());

    WidgetsBinding.instance.addPostFrameCallback((_) => safeSetState(() {}));
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    context.watch<FFAppState>();

    return GestureDetector(
      onTap: () {
        FocusScope.of(context).unfocus();
        FocusManager.instance.primaryFocus?.unfocus();
      },
      child: Scaffold(
        key: scaffoldKey,

        backgroundColor: FlutterFlowTheme.of(context).primaryBackground,

        appBar: AppBar(
          backgroundColor: FlutterFlowTheme.of(context).primary,

          automaticallyImplyLeading: true,

          actions: [],

          centerTitle: true,

          elevation: 0.0,
        ),
        body: SafeArea(
          top: true,
          child: Column(
            mainAxisSize: MainAxisSize.max,

            children: [
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(16.0, 16.0, 16.0, 16.0),
                child: Builder(
                  builder: (context) {
                    final celularAtual = FFAppState().listaResultados.toList();

                    return ListView.builder(
                      padding: EdgeInsets.zero,

                      shrinkWrap: true,
                      scrollDirection: Axis.vertical,
                      itemCount: celularAtual.length,

                      itemBuilder: (context, celularAtualIndex) {
                        final celularAtualItem =
                            celularAtual[celularAtualIndex];
                        return Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                            12.0,
                            12.0,
                            12.0,
                            12.0,
                          ),
                          child: Material(
                            color: Colors.transparent,
                            elevation: 2.0,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.only(
                                bottomLeft: Radius.circular(12.0),
                                bottomRight: Radius.circular(12.0),
                                topLeft: Radius.circular(12.0),
                                topRight: Radius.circular(12.0),
                              ),
                            ),
                            child: Container(
                              width: double.infinity,
                              height: 120.0,

                              decoration: BoxDecoration(
                                color: FlutterFlowTheme.of(
                                  context,
                                ).secondaryBackground,

                                borderRadius: BorderRadius.only(
                                  bottomLeft: Radius.circular(12.0),
                                  bottomRight: Radius.circular(12.0),
                                  topLeft: Radius.circular(12.0),
                                  topRight: Radius.circular(12.0),
                                ),
                              ),

                              child: Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                  12.0,
                                  12.0,
                                  12.0,
                                  12.0,
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.max,

                                  children: [
                                    Opacity(
                                      opacity: getJsonField(
                                        celularAtualItem,
                                        r'''$.imagem''',
                                      ),
                                      child: ClipRRect(
                                        borderRadius: BorderRadius.only(
                                          bottomLeft: Radius.circular(8.0),
                                          bottomRight: Radius.circular(8.0),
                                          topLeft: Radius.circular(8.0),
                                          topRight: Radius.circular(8.0),
                                        ),
                                        child: Image.network(
                                          'https://picsum.photos/seed/232/600',
                                          width: 82.0,
                                          height: 82.0,
                                          fit: BoxFit.cover,
                                        ),
                                      ),
                                    ),
                                    Column(
                                      mainAxisSize: MainAxisSize.max,
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,

                                      children: [
                                        Padding(
                                          padding:
                                              EdgeInsetsDirectional.fromSTEB(
                                                25.0,
                                                0.0,
                                                0.0,
                                                0.0,
                                              ),
                                          child: Text(
                                            valueOrDefault<String>(
                                              getJsonField(
                                                celularAtualItem,
                                                r'''$.nome''',
                                              )?.toString(),
                                              'Carregando...',
                                            ),

                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                                  font: GoogleFonts.montserrat(
                                                    fontWeight: FontWeight.bold,
                                                    fontStyle:
                                                        FlutterFlowTheme.of(
                                                          context,
                                                        ).bodyMedium.fontStyle,
                                                  ),

                                                  fontSize: 17.0,
                                                  letterSpacing: 0.0,
                                                  fontWeight: FontWeight.bold,
                                                  fontStyle:
                                                      FlutterFlowTheme.of(
                                                        context,
                                                      ).bodyMedium.fontStyle,
                                                ),
                                          ),
                                        ),
                                        Padding(
                                          padding:
                                              EdgeInsetsDirectional.fromSTEB(
                                                25.0,
                                                0.0,
                                                0.0,
                                                0.0,
                                              ),
                                          child: Text(
                                            getJsonField(
                                              celularAtualItem,
                                              r'''$.preco''',
                                            ).toString(),

                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                                  font: GoogleFonts.montserrat(
                                                    fontWeight: FontWeight.bold,
                                                    fontStyle:
                                                        FlutterFlowTheme.of(
                                                          context,
                                                        ).bodyMedium.fontStyle,
                                                  ),

                                                  color: Color(0xFF08FF08),

                                                  letterSpacing: 0.0,
                                                  fontWeight: FontWeight.bold,
                                                  fontStyle:
                                                      FlutterFlowTheme.of(
                                                        context,
                                                      ).bodyMedium.fontStyle,
                                                ),
                                          ),
                                        ),
                                        Padding(
                                          padding:
                                              EdgeInsetsDirectional.fromSTEB(
                                                25.0,
                                                0.0,
                                                0.0,
                                                0.0,
                                              ),
                                          child: Text(
                                            getJsonField(
                                              celularAtualItem,
                                              r'''$.motivo''',
                                            ).toString(),

                                            style: FlutterFlowTheme.of(context)
                                                .bodyMedium
                                                .override(
                                                  fontFamily:
                                                      FlutterFlowTheme.of(
                                                        context,
                                                      ).bodyMediumFamily,
                                                  color: Color(0xFF3296E4),

                                                  letterSpacing: 0.0,
                                                  fontWeight: FontWeight.bold,

                                                  useGoogleFonts:
                                                      !FlutterFlowTheme.of(
                                                        context,
                                                      ).bodyMediumIsCustom,
                                                ),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
