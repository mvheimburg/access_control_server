///
//  Generated code. Do not modify.
//  source: accesscontrol.proto
//
// @dart = 2.3
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type

import 'dart:async' as $async;

import 'dart:core' as $core;

import 'package:grpc/service_api.dart' as $grpc;
import 'accesscontrol.pb.dart' as $0;
export 'accesscontrol.pb.dart';

class AccessControlClient extends $grpc.Client {
  static final _$dingDong =
      $grpc.ClientMethod<$0.DingDongRequest, $0.DingDongReply>(
          '/accesscontrol.AccessControl/DingDong',
          ($0.DingDongRequest value) => value.writeToBuffer(),
          ($core.List<$core.int> value) => $0.DingDongReply.fromBuffer(value));

  AccessControlClient($grpc.ClientChannel channel, {$grpc.CallOptions options})
      : super(channel, options: options);

  $grpc.ResponseFuture<$0.DingDongReply> dingDong($0.DingDongRequest request,
      {$grpc.CallOptions options}) {
    final call = $createCall(_$dingDong, $async.Stream.fromIterable([request]),
        options: options);
    return $grpc.ResponseFuture(call);
  }
}

abstract class AccessControlServiceBase extends $grpc.Service {
  $core.String get $name => 'accesscontrol.AccessControl';

  AccessControlServiceBase() {
    $addMethod($grpc.ServiceMethod<$0.DingDongRequest, $0.DingDongReply>(
        'DingDong',
        dingDong_Pre,
        false,
        false,
        ($core.List<$core.int> value) => $0.DingDongRequest.fromBuffer(value),
        ($0.DingDongReply value) => value.writeToBuffer()));
  }

  $async.Future<$0.DingDongReply> dingDong_Pre(
      $grpc.ServiceCall call, $async.Future<$0.DingDongRequest> request) async {
    return dingDong(call, await request);
  }

  $async.Future<$0.DingDongReply> dingDong(
      $grpc.ServiceCall call, $0.DingDongRequest request);
}
