"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;
var _createNewSentence = require("./createNewSentence");
var _createNewWord = require("./createNewWord");
var _getAllSentences = require("./getAllSentences");
var _getAllWords = require("./getAllWords");
var _default = [_createNewSentence.createNewSentenceRoute, _createNewWord.createNewWordRoute, _getAllSentences.getAllSentencesRoute, _getAllWords.getAllWordsRoute];
exports["default"] = _default;