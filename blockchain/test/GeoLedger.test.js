const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("GeoLedger", function () {
  let geoLedger;
  let owner;
  let userOne;
  let userTwo;

  beforeEach(async function () {
    [owner, userOne, userTwo] = await ethers.getSigners();

    const GeoLedger = await ethers.getContractFactory("GeoLedger");
    geoLedger = await GeoLedger.deploy();

    await geoLedger.waitForDeployment();
  });

  it("should deploy successfully", async function () {
    expect(await geoLedger.getNextDatasetId()).to.equal(1);
  });

  it("should create a dataset", async function () {
    const tx = await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await expect(tx).to.emit(geoLedger, "DatasetCreated");

    const dataset = await geoLedger.getDataset(1);

    expect(dataset[0]).to.equal(1);
    expect(dataset[1]).to.equal(owner.address);
    expect(dataset[2]).to.equal("Smart City Roads");
    expect(dataset[3]).to.equal("QmExampleCid123");
    expect(dataset[4]).to.equal("0xexamplehash123");
  });

  it("should give dataset owner access automatically", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    const hasAccess = await geoLedger.hasAccess(1, owner.address);

    expect(hasAccess).to.equal(true);
  });

  it("should allow owner to grant access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await expect(geoLedger.grantAccess(1, userOne.address)).to.emit(
      geoLedger,
      "AccessGranted"
    );

    const hasAccess = await geoLedger.hasAccess(1, userOne.address);

    expect(hasAccess).to.equal(true);
  });

  it("should allow owner to revoke access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await geoLedger.grantAccess(1, userOne.address);
    await geoLedger.revokeAccess(1, userOne.address);

    const hasAccess = await geoLedger.hasAccess(1, userOne.address);

    expect(hasAccess).to.equal(false);
  });

  it("should not allow non-owner to grant access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await expect(
      geoLedger.connect(userOne).grantAccess(1, userTwo.address)
    ).to.be.revertedWith("Only dataset owner can perform this action");
  });

  it("should not allow non-owner to revoke access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await geoLedger.grantAccess(1, userOne.address);

    await expect(
      geoLedger.connect(userOne).revokeAccess(1, userOne.address)
    ).to.be.revertedWith("Only dataset owner can perform this action");
  });

  it("should not allow unauthorized user to record dataset access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await expect(
      geoLedger.connect(userOne).recordDatasetAccess(1)
    ).to.be.revertedWith("User does not have access");
  });

  it("should allow authorized user to record dataset access", async function () {
    await geoLedger.createDataset(
      "Smart City Roads",
      "QmExampleCid123",
      "0xexamplehash123"
    );

    await geoLedger.grantAccess(1, userOne.address);

    await expect(geoLedger.connect(userOne).recordDatasetAccess(1)).to.emit(
      geoLedger,
      "DatasetAccessed"
    );
  });
});