//
//  ReminisiaApp.swift
//  Reminisia
//
//  Created by Yunfan Yang on 4/3/23.
//

import SwiftUI

@main
struct ReminisiaApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
