///
//  Generated code. Do not modify.
//  source: mqttguide.proto
//
// @dart = 2.3
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type

import 'dart:async' as $async;

import 'dart:core' as $core;

import 'package:grpc/service_api.dart' as $grpc;
import 'mqttguide.pb.dart' as $0;
export 'mqttguide.pb.dart';

class MqttGuideClient extends $grpc.Client {
  static final _$dingDong = $grpc.ClientMethod<$0.DingDongArgs, $0.DingDongRet>(
      '/mqttguide.MqttGuide/DingDong',
      ($0.DingDongArgs value) => value.writeToBuffer(),
      ($core.List<$core.int> value) => $0.DingDongRet.fromBuffer(value));

  MqttGuideClient($grpc.ClientChannel channel, {$grpc.CallOptions options})
      : super(channel, options: options);

  $grpc.ResponseFuture<$0.DingDongRet> dingDong($0.DingDongArgs request,
      {$grpc.CallOptions options}) {
    final call = $createCall(_$dingDong, $async.Stream.fromIterable([request]),
        options: options);
    return $grpc.ResponseFuture(call);
  }
}

abstract class MqttGuideServiceBase extends $grpc.Service {
  $core.String get $name => 'mqttguide.MqttGuide';

  MqttGuideServiceBase() {
    $addMethod($grpc.ServiceMethod<$0.DingDongArgs, $0.DingDongRet>(
        'DingDong',
        dingDong_Pre,
        false,
        false,
        ($core.List<$core.int> value) => $0.DingDongArgs.fromBuffer(value),
        ($0.DingDongRet value) => value.writeToBuffer()));
  }

  $async.Future<$0.DingDongRet> dingDong_Pre(
      $grpc.ServiceCall call, $async.Future<$0.DingDongArgs> request) async {
    return dingDong(call, await request);
  }

  $async.Future<$0.DingDongRet> dingDong(
      $grpc.ServiceCall call, $0.DingDongArgs request);
}
