#!/usr/bin/env node
import { createClient, print } from 'redis';

const client = createClient();

const data = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

Object.entries(data).forEach(([k, v]) => { client.hset('HolbertonSchools', k, v, print); })
client.hgetall('HolbertonSchools', (err, val) => { console.log(val) })
