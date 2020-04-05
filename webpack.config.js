const webpack = require('webpack');
const path = require('path');

const config = {
  entry: {
      'app': path.resolve(__dirname,'./world/static/app.js')
    },
  output: {
    path: path.resolve(__dirname, 'world/static/'),
    filename: '[name].bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader',
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
    new webpack.SourceMapDevToolPlugin({})
  ],
  /*
  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }*/
};

module.exports = config;