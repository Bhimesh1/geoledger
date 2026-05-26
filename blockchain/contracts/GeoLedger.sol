// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract GeoLedger {
    struct Dataset {
        uint256 id;
        address owner;
        string name;
        string ipfsCid;
        string fileHash;
        uint256 createdAt;
        bool exists;
    }

    uint256 private nextDatasetId;

    mapping(uint256 => Dataset) private datasets;
    mapping(uint256 => mapping(address => bool)) private datasetAccess;

    event DatasetCreated(
        uint256 indexed datasetId,
        address indexed owner,
        string name,
        string ipfsCid,
        string fileHash,
        uint256 createdAt
    );

    event AccessGranted(
        uint256 indexed datasetId,
        address indexed owner,
        address indexed user,
        uint256 timestamp
    );

    event AccessRevoked(
        uint256 indexed datasetId,
        address indexed owner,
        address indexed user,
        uint256 timestamp
    );

    event DatasetAccessed(
        uint256 indexed datasetId,
        address indexed user,
        uint256 timestamp
    );

    modifier datasetExists(uint256 datasetId) {
        require(datasets[datasetId].exists, "Dataset does not exist");
        _;
    }

    modifier onlyDatasetOwner(uint256 datasetId) {
        require(datasets[datasetId].owner == msg.sender, "Only dataset owner can perform this action");
        _;
    }

    constructor() {
        nextDatasetId = 1;
    }

    function createDataset(
        string memory name,
        string memory ipfsCid,
        string memory fileHash
    ) external returns (uint256) {
        require(bytes(name).length > 0, "Dataset name is required");
        require(bytes(ipfsCid).length > 0, "IPFS CID is required");
        require(bytes(fileHash).length > 0, "File hash is required");

        uint256 datasetId = nextDatasetId;

        datasets[datasetId] = Dataset({
            id: datasetId,
            owner: msg.sender,
            name: name,
            ipfsCid: ipfsCid,
            fileHash: fileHash,
            createdAt: block.timestamp,
            exists: true
        });

        datasetAccess[datasetId][msg.sender] = true;

        nextDatasetId++;

        emit DatasetCreated(
            datasetId,
            msg.sender,
            name,
            ipfsCid,
            fileHash,
            block.timestamp
        );

        return datasetId;
    }

    function grantAccess(
        uint256 datasetId,
        address user
    )
        external
        datasetExists(datasetId)
        onlyDatasetOwner(datasetId)
    {
        require(user != address(0), "Invalid user address");
        require(user != msg.sender, "Owner already has access");

        datasetAccess[datasetId][user] = true;

        emit AccessGranted(datasetId, msg.sender, user, block.timestamp);
    }

    function revokeAccess(
        uint256 datasetId,
        address user
    )
        external
        datasetExists(datasetId)
        onlyDatasetOwner(datasetId)
    {
        require(user != address(0), "Invalid user address");
        require(user != msg.sender, "Owner access cannot be revoked");

        datasetAccess[datasetId][user] = false;

        emit AccessRevoked(datasetId, msg.sender, user, block.timestamp);
    }

    function hasAccess(
        uint256 datasetId,
        address user
    )
        external
        view
        datasetExists(datasetId)
        returns (bool)
    {
        return datasetAccess[datasetId][user];
    }

    function getDataset(
        uint256 datasetId
    )
        external
        view
        datasetExists(datasetId)
        returns (
            uint256 id,
            address owner,
            string memory name,
            string memory ipfsCid,
            string memory fileHash,
            uint256 createdAt
        )
    {
        Dataset memory dataset = datasets[datasetId];

        return (
            dataset.id,
            dataset.owner,
            dataset.name,
            dataset.ipfsCid,
            dataset.fileHash,
            dataset.createdAt
        );
    }

    function recordDatasetAccess(
        uint256 datasetId
    )
        external
        datasetExists(datasetId)
    {
        require(datasetAccess[datasetId][msg.sender], "User does not have access");

        emit DatasetAccessed(datasetId, msg.sender, block.timestamp);
    }

    function getNextDatasetId() external view returns (uint256) {
        return nextDatasetId;
    }
}