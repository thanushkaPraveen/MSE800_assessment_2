abstract class AppResponse<T> {
  final int code;
  final String message;
  final T? data;

  AppResponse({required this.code, required this.message, this.data});

  @override
  String toString() {
    return 'AppResponse(code: $code, message: $message, data: $data)';
  }
}

class SuccessResponse<T> extends AppResponse<T> {
  SuccessResponse({required int code, required String message, T? data})
      : super(code: code, message: message, data: data);

  @override
  String toString() {
    return 'SuccessResponse(code: $code, message: $message, data: $data)';
  }
}

class ErrorResponse extends AppResponse<Null> {
  ErrorResponse({required int code, required String message})
      : super(code: code, message: message);

  @override
  String toString() {
    return 'ErrorResponse(code: $code, message: $message)';
  }
}
