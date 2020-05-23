var admin = require('firebase-admin');
var serviceAccount = require("./akbtest-66d57-firebase-adminsdk-a03es-e7698cd958.json");

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore()
const fs = require('fs')
const csvSync = require('csv-parse/lib/sync')
const artname = process.argv[2]

const file = '../songlist/' + artname + '.csv' //インポートしたいcsvファイルをindex.jsと同じ階層に入れてください
let tournaments = fs.readFileSync(file) //csvファイルの読み込み
let responses = csvSync(tournaments)//parse csv
let objects = [] //この配列の中にパースしたcsvの中身をkey-value形式で入れていく。
const docname = db.collection('tournaments').doc(process.argv[3])

docname.set({name: artname + 'のトーナメント'})
responses.forEach(function(response){
  docname.collection('players').doc().set({ name: response.toString() })
}, this)