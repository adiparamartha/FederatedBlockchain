/**
 *Submitted for verification at Etherscan.io on 2022-10-22
 */

// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract FedL2 {
    uint256 number;
    uint256 add;

    uint256 client_id;
    string parameter;
    uint256[] list_of_clients;
    string[] list_of_parameter;

    function store_param(uint256 id, string memory param) public {
        client_id = id;
        parameter = param;
        list_of_clients.push(client_id);
        list_of_parameter.push(parameter);
    }

    function aggregate_param()
        public
        view
        returns (
            uint256[] memory,
            string[] memory,
            uint256 sum,
            uint256 avg
        )
    {
        for (uint256 i = 0; i < list_of_clients.length; i++) {
            sum += list_of_clients[i];
        }
        avg = sum / list_of_clients.length;
        return (list_of_clients, list_of_parameter, sum, avg);
    }
}
