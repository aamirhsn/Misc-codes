#!/usr/bin/python3

import boto3
from time import sleep
from datetime import datetime

VaultNameU = "Default"

def get_recovery_points(vault_name):
    pagination = True
    restore_points = []
    b = boto3.client('backup')

    res = b.list_recovery_points_by_backup_vault(
        BackupVaultName=VaultNameU,
        MaxResults=100
    )

    while pagination:
        for point in res['RecoveryPoints']:
            if (point['Status'])=='EXPIRED':
                restore_points.append(point['RecoveryPointArn'])
            
        if 'NextToken' in res:
            res = b.list_recovery_points_by_backup_vault(
                BackupVaultName=VaultNameU,
                MaxResults=100,
                NextToken=res['NextToken']
            )
        else:
            pagination = False

    return restore_points
    
def delete_recovery_points(vault_name: str, point_arn_list: list) -> bool:
    b = boto3.client('backup')

    for index, point in enumerate(point_arn_list):
        print(f'[.] Deleting recovery point "{point}" [{index} / {len(point_arn_list)}]')
        res = b.delete_recovery_point(
            BackupVaultName=VaultNameU,
            RecoveryPointArn=point
        )
        sleep(1)

    return True
    
def backup(event, context):
    vault_name = VaultNameU
    recovery_points = get_recovery_points(VaultNameU)
    print(f'[+] Found {len(recovery_points)} Recovery Points! Deleting them!:{(recovery_points)}')
    delete_recovery_points(VaultNameU, recovery_points)
