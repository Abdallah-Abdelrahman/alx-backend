#!/usr/bin/env node
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get.bind(client));
  const val = await get(schoolName)
  console.log(val);
}

displaySchoolValue('Holberton')
  .then(setNewSchool.bind(null, 'HolbertonSanFrancisco', '100'))
  .then(displaySchoolValue.bind(null, 'HolbertonSanFrancisco'))
