"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/interopRequireDefault");
Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.createNewSentenceRoute = void 0;
var _regenerator = _interopRequireDefault(require("@babel/runtime/regenerator"));
var _asyncToGenerator2 = _interopRequireDefault(require("@babel/runtime/helpers/asyncToGenerator"));
var _database = require("../database");
var createNewSentenceRoute = {
  method: 'POST',
  path: '/api/sentence',
  handler: function () {
    var _handler = (0, _asyncToGenerator2["default"])( /*#__PURE__*/_regenerator["default"].mark(function _callee(req, h) {
      var sentence;
      return _regenerator["default"].wrap(function _callee$(_context) {
        while (1) switch (_context.prev = _context.next) {
          case 0:
            console.log(req.payload);
            sentence = req.payload.sentence;
            _context.next = 4;
            return _database.db.query('INSERT INTO sentences (id, sentence) VALUES (null, ?)', sentence);
          case 4:
            return _context.abrupt("return", sentence);
          case 5:
          case "end":
            return _context.stop();
        }
      }, _callee);
    }));
    function handler(_x, _x2) {
      return _handler.apply(this, arguments);
    }
    return handler;
  }()
};
exports.createNewSentenceRoute = createNewSentenceRoute;