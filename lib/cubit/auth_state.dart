import 'dart:math';

import 'package:equatable/equatable.dart';
import 'package:flutter/material.dart';
import '../data/models/user_model.dart';

abstract class AuthState extends Equatable {
  @override
  List<Object?> get props => [];
}

class AuthInitial extends AuthState {
  final index = Random().nextInt(100);

  @override
  List<Object?> get props => [index];
}

class AuthLoading extends AuthState {}

class AuthSuccess extends AuthState {
  final UserModel user;
  AuthSuccess(this.user);
}

class AuthFailure extends AuthState {
  final String error;
  AuthFailure(this.error);
}
