///
//  Generated code. Do not modify.
//  source: accesscontrol.proto
//
// @dart = 2.3
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name,return_of_invalid_type

import 'dart:core' as $core;

import 'package:protobuf/protobuf.dart' as $pb;

class DingDongRequest extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('DingDongRequest', package: const $pb.PackageName('accesscontrol'), createEmptyInstance: create)
    ..aOS(1, 'message')
    ..hasRequiredFields = false
  ;

  DingDongRequest._() : super();
  factory DingDongRequest() => create();
  factory DingDongRequest.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromBuffer(i, r);
  factory DingDongRequest.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromJson(i, r);
  DingDongRequest clone() => DingDongRequest()..mergeFromMessage(this);
  DingDongRequest copyWith(void Function(DingDongRequest) updates) => super.copyWith((message) => updates(message as DingDongRequest));
  $pb.BuilderInfo get info_ => _i;
  @$core.pragma('dart2js:noInline')
  static DingDongRequest create() => DingDongRequest._();
  DingDongRequest createEmptyInstance() => create();
  static $pb.PbList<DingDongRequest> createRepeated() => $pb.PbList<DingDongRequest>();
  @$core.pragma('dart2js:noInline')
  static DingDongRequest getDefault() => _defaultInstance ??= $pb.GeneratedMessage.$_defaultFor<DingDongRequest>(create);
  static DingDongRequest _defaultInstance;

  @$pb.TagNumber(1)
  $core.String get message => $_getSZ(0);
  @$pb.TagNumber(1)
  set message($core.String v) { $_setString(0, v); }
  @$pb.TagNumber(1)
  $core.bool hasMessage() => $_has(0);
  @$pb.TagNumber(1)
  void clearMessage() => clearField(1);
}

class DingDongReply extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('DingDongReply', package: const $pb.PackageName('accesscontrol'), createEmptyInstance: create)
    ..aOS(1, 'message')
    ..hasRequiredFields = false
  ;

  DingDongReply._() : super();
  factory DingDongReply() => create();
  factory DingDongReply.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromBuffer(i, r);
  factory DingDongReply.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) => create()..mergeFromJson(i, r);
  DingDongReply clone() => DingDongReply()..mergeFromMessage(this);
  DingDongReply copyWith(void Function(DingDongReply) updates) => super.copyWith((message) => updates(message as DingDongReply));
  $pb.BuilderInfo get info_ => _i;
  @$core.pragma('dart2js:noInline')
  static DingDongReply create() => DingDongReply._();
  DingDongReply createEmptyInstance() => create();
  static $pb.PbList<DingDongReply> createRepeated() => $pb.PbList<DingDongReply>();
  @$core.pragma('dart2js:noInline')
  static DingDongReply getDefault() => _defaultInstance ??= $pb.GeneratedMessage.$_defaultFor<DingDongReply>(create);
  static DingDongReply _defaultInstance;

  @$pb.TagNumber(1)
  $core.String get message => $_getSZ(0);
  @$pb.TagNumber(1)
  set message($core.String v) { $_setString(0, v); }
  @$pb.TagNumber(1)
  $core.bool hasMessage() => $_has(0);
  @$pb.TagNumber(1)
  void clearMessage() => clearField(1);
}

