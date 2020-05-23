var admin = require('firebase-admin');

var serviceAccount = require("./akbtest-66d57-firebase-adminsdk-a03es-e7698cd958.json");

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount)
    //databaseURL: "https://[projectID].firebaseio.com"
});


const db = admin.firestore()
const fs = require('fs')


let documentRef = db.doc('col/doc');
let subcollection = documentRef.collection('subcollection');
console.log(`Path to subcollection: ${subcollection.path}`);




let sfRef = db.collection('tournaments').doc();
sfRef.getCollections().then(collections => {
  collections.forEach(collection => {
    console.log('Found subcollection with id:', collection.id);
  });
});