///
//  Generated code. Do not modify.
//  source: mqttguide.proto
//
// @dart = 2.3
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type

import 'dart:core' as $core;

import 'package:protobuf/protobuf.dart' as $pb;

class DingDongArgs extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('DingDongArgs', package: const $pb.PackageName('mqttguide'), createEmptyInstance: create)
    ..hasRequiredFields = false
  ;

  DingDongArgs._() : super();
  factory DingDongArgs() => create();
  factory DingDongArgs.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromBuffer(i, r);
  factory DingDongArgs.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromJson(i, r);
  DingDongArgs clone() => DingDongArgs()..mergeFromMessage(this);
  DingDongArgs copyWith(void Function(DingDongArgs) updates) => super.copyWith((message) => updates(message as DingDongArgs));
  $pb.BuilderInfo get info_ => _i;
  @$core.pragma('dart2js:noInline')
  static DingDongArgs create() => DingDongArgs._();
  DingDongArgs createEmptyInstance() => create();
  static $pb.PbList<DingDongArgs> createRepeated() => $pb.PbList<DingDongArgs>();
  @$core.pragma('dart2js:noInline')
  static DingDongArgs getDefault() => _defaultInstance ??= $pb.GeneratedMessage.$_defaultFor<DingDongArgs>(create);
  static DingDongArgs _defaultInstance;
}

class DingDongRet extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('DingDongRet', package: const $pb.PackageName('mqttguide'), createEmptyInstance: create)
    ..hasRequiredFields = false
  ;

  DingDongRet._() : super();
  factory DingDongRet() => create();
  factory DingDongRet.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromBuffer(i, r);
  factory DingDongRet.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromJson(i, r);
  DingDongRet clone() => DingDongRet()..mergeFromMessage(this);
  DingDongRet copyWith(void Function(DingDongRet) updates) => super.copyWith((message) => updates(message as DingDongRet));
  $pb.BuilderInfo get info_ => _i;
  @$core.pragma('dart2js:noInline')
  static DingDongRet create() => DingDongRet._();
  DingDongRet createEmptyInstance() => create();
  static $pb.PbList<DingDongRet> createRepeated() => $pb.PbList<DingDongRet>();
  @$core.pragma('dart2js:noInline')
  static DingDongRet getDefault() => _defaultInstance ??= $pb.GeneratedMessage.$_defaultFor<DingDongRet>(create);
  static DingDongRet _defaultInstance;
}

