---
title: "BasicAlertDialog"
description: "A Jetpack Compose BasicAlertDialog component for displaying dialogs with custom content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/basicalertdialog.md"
scraped_at: "2026-07-15T09:00:35.681136"
---

---
title: BasicAlertDialog
description: A Jetpack Compose BasicAlertDialog component for displaying dialogs with custom content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# BasicAlertDialog

A Jetpack Compose BasicAlertDialog component for displaying dialogs with custom content.
Android, Included in Expo Go

Expo UI BasicAlertDialog matches the official Jetpack Compose [BasicAlertDialog](https://developer.android.com/develop/ui/compose/components/dialog) API and displays a minimal dialog that accepts custom children as its content, giving you full control over the dialog layout.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic dialog with custom content

```tsx
import { useState } from 'react';
import {
  Host,
  BasicAlertDialog,
  Button,
  TextButton,
  Text,
  Surface,
  Column,
  Spacer,
} from '@expo/ui/jetpack-compose';
import {
  padding,
  wrapContentWidth,
  wrapContentHeight,
  clip,
  height,
  align,
  Shapes,
} from '@expo/ui/jetpack-compose/modifiers';

export default function BasicAlertDialogExample() {
  const [visible, setVisible] = useState(false);

  return (
    <Host matchContents>
      <Button onClick={() => setVisible(true)}>
        <Text>Open dialog</Text>
      </Button>
      {visible && (
        <BasicAlertDialog onDismissRequest={() => setVisible(false)}>
          <Surface
            tonalElevation={6}
            modifiers={[wrapContentWidth(), wrapContentHeight(), clip(Shapes.RoundedCorner(28))]}>
            <Column modifiers={[padding(16, 16, 16, 16)]}>
              <Text>
                This area typically contains the supportive text which presents the details
                regarding the Dialog's purpose.
              </Text>
              <Spacer modifiers={[height(24)]} />
              <TextButton onClick={() => setVisible(false)} modifiers={[align('centerEnd')]}>
                <Text>Confirm</Text>
              </TextButton>
            </Column>
          </Surface>
        </BasicAlertDialog>
      )}
    </Host>
  );
}
```

## API

```tsx
import { BasicAlertDialog } from '@expo/ui/jetpack-compose';
```

## Component

### `BasicAlertDialog`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BasicAlertDialogProps](#basicalertdialogprops)\>

A basic alert dialog that provides a blank container for custom content. Unlike `AlertDialog`, this component does not have structured title/text/buttons slots.

BasicAlertDialogProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the dialog.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDismissRequest`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the user tries to dismiss the dialog (e.g. by tapping outside of it or pressing the back button).

### `properties`

Supported platforms: Android.

Optional • Type: [DialogProperties](#dialogproperties)

Properties for the dialog window.

## Types

### `DialogProperties`

Supported platforms: Android.

Properties for the dialog window, matching `DialogProperties` in Compose.

| Property | Type | Description |
| --- | --- | --- |
| decorFitsSystemWindows(optional) | `boolean` | Whether the dialog's decor fits system windows (status bar, navigation bar, and more). When `true`, the dialog's content will be inset to avoid overlapping with system UI. Default: `true` |
| dismissOnBackPress(optional) | `boolean` | Whether the dialog can be dismissed by pressing the back button. Default: `true` |
| dismissOnClickOutside(optional) | `boolean` | Whether the dialog can be dismissed by clicking outside of it. Default: `true` |
| usePlatformDefaultWidth(optional) | `boolean` | Whether the dialog should use the platform default width. Default: `true` |
