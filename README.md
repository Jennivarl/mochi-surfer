# Mochi Surfer

A mochi-themed skateboarding game with an on-chain leaderboard powered by GenLayer.

## Play

[https://mochi-surfer.vercel.app](https://mochi-surfer.vercel.app)

## What it does

- Endless runner where you dodge obstacles and collect coins
- Scores are saved on-chain using a GenLayer intelligent contract
- AI validators check usernames before they go on the leaderboard
- Connect your wallet to submit scores
- Create tournament rooms and play with friends in real time

## Contract

- **Address:** `0x6Ec313A838bc657b4d928B56cd91C82C718613F1`
- **Network:** GenLayer Testnet (Chain ID 4221)
- **RPC:** `https://rpc-bradbury.genlayer.com`

## Tech

- Single-file HTML5 game (vanilla JS + Canvas)
- GenLayer intelligent contract with `run_nondet_unsafe` for AI username moderation
- genlayer-js SDK for on-chain reads/writes
- Firebase Realtime Database for multiplayer room sync
- EIP-6963 wallet discovery (MetaMask, etc.)
