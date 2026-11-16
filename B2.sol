
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {

    uint public balance;

    // Deposit Ether
    function deposit() public payable {
        balance = balance + msg.value;
    }

    // Withdraw Ether
    function withdraw(uint amount) public {
        require(amount <= balance, "Insufficient Balance");

        balance = balance - amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");

        require(success, "Transaction Failed");
    }

    // Show Balance
    function showBalance() public view returns(uint) {
        return balance;
    }
}

