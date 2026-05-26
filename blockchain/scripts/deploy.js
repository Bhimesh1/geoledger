const hre = require("hardhat");

async function main() {
  console.log("Deploying GeoLedger smart contract...");

  const GeoLedger = await hre.ethers.getContractFactory("GeoLedger");
  const geoLedger = await GeoLedger.deploy();

  await geoLedger.waitForDeployment();

  const contractAddress = await geoLedger.getAddress();

  console.log("GeoLedger deployed to:", contractAddress);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});